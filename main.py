import tkinter as tk
from tkinter import ttk
import re
import math

class PasswordStrengthChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("400x300")
        
        # Configure styles for progress bar
        self.style = ttk.Style()
        self.style.configure("TProgressbar", thickness=20)
        
        # Create and pack widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Password entry
        self.password_label = tk.Label(self.root, text="Enter Password:", font=("Arial", 12))
        self.password_label.pack(pady=10)
        
        self.password_var = tk.StringVar()
        self.password_var.trace('w', self.check_password)
        self.password_entry = tk.Entry(self.root, textvariable=self.password_var, show="*", width=30, font=("Arial", 12))
        self.password_entry.pack(pady=5)
        
        # Strength indicator label
        self.strength_var = tk.StringVar(value="Strength: None")
        self.strength_label = tk.Label(self.root, textvariable=self.strength_var, font=("Arial", 12, "bold"))
        self.strength_label.pack(pady=5)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.root, length=200, mode='determinate', style="TProgressbar")
        self.progress.pack(pady=5)
        
        # Feedback area
        self.feedback_text = tk.Text(self.root, height=8, width=40, wrap=tk.WORD, font=("Arial", 10))
        self.feedback_text.pack(pady=10)
        
    def calculate_entropy(self, password):
        char_set_size = 0
        if re.search(r'[a-z]', password): char_set_size += 26
        if re.search(r'[A-Z]', password): char_set_size += 26
        if re.search(r'[0-9]', password): char_set_size += 10
        if re.search(r'[^a-zA-Z0-9]', password): char_set_size += 32
        
        entropy = len(password) * math.log2(max(char_set_size, 1))
        return entropy
        
    def check_password(self, *args):
        password = self.password_var.get()
        feedback = []
        score = 0
        max_score = 100
        
        # Length check
        if len(password) == 0:
            self.strength_var.set("Strength: None")
            self.progress['value'] = 0
            self.feedback_text.delete(1.0, tk.END)
            return
        elif len(password) < 8:
            feedback.append("• Password should be at least 8 characters long")
        else:
            score += 20
            
        # Uppercase check
        if not re.search(r'[A-Z]', password):
            feedback.append("• Include at least one uppercase letter")
        else:
            score += 20
            
        # Lowercase check
        if not re.search(r'[a-z]', password):
            feedback.append("• Include at least one lowercase letter")
        else:
            score += 20
            
        # Number check
        if not re.search(r'[0-9]', password):
            feedback.append("• Include at least one number")
        else:
            score += 20
            
        # Special character check
        if not re.search(r'[^a-zA-Z0-9]', password):
            feedback.append("• Include at least one special character")
        else:
            score += 20
            
        # Common patterns check
        common_patterns = [
            r'12345', r'qwerty', r'password', r'admin', r'abc123',
            r'(\w)\1{2,}',  # Repeated characters
            r'(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',  # Sequential letters
        ]
        
        for pattern in common_patterns:
            if re.search(pattern, password.lower()):
                feedback.append("• Avoid common patterns and sequences")
                score = max(0, score - 20)
                break
                
        # Entropy bonus
        entropy = self.calculate_entropy(password)
        if entropy > 60:
            score = min(100, score + 10)
        
        # Update progress bar
        self.progress['value'] = score
        
        # Update progress bar color and strength text
        if score >= 90:
            self.progress.configure(style="TProgressbar")
            self.progress['style'] = "TProgressbar"
            self.strength_var.set("Strength: Perfect!")
            self.strength_label.configure(fg="dark green")
        elif score >= 80:
            self.strength_var.set("Strength: Very Strong")
            self.strength_label.configure(fg="green")
        elif score >= 60:
            self.strength_var.set("Strength: Strong")
            self.strength_label.configure(fg="blue")
        elif score >= 40:
            self.strength_var.set("Strength: Moderate")
            self.strength_label.configure(fg="orange")
        else:
            self.strength_var.set("Strength: Weak")
            self.strength_label.configure(fg="red")
            
        # Update feedback text
        self.feedback_text.delete(1.0, tk.END)
        if feedback:
            self.feedback_text.insert(tk.END, "Suggestions to improve password strength:\n\n")
            self.feedback_text.insert(tk.END, "\n".join(feedback))
        else:
            self.feedback_text.insert(tk.END, "Strong password! ✓\nYour password meets all security requirements.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()
