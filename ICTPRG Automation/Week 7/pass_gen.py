import requests
import random
import hashlib

url = "https://raw.githubusercontent.com/josuamarcelc/common-password-list/main/rockyou.txt/rockyou_1.txt"
response = requests.get(url)
lines = response.text.split("\n")
count = len(lines)

pwNum = random.randint(1, count)
pwText = lines[pwNum].rstrip()

# Calculate md5sum
md5sum = hashlib.md5(pwText.encode('utf-8')).hexdigest()

# Replace characters with leetspeak
leetspeak_dict = {
    '0': '0',
    '1': '!',
    '2': '@',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'a': '4',
    'b': '6',
    'c': '(',  # Use parentheses for 'c'
    'd': 'd',
    'e': '3',
    'f': 'ph'  # Use 'ph' for 'f'
}

md5sum_leet = ''.join(leetspeak_dict.get(c, c) for c in md5sum)

# Add some random leetspeak characters
for i in range(random.randint(1, 3)):
    index = random.randint(0, len(md5sum_leet) - 1)
    char = random.choice(list(leetspeak_dict.values()))
    md5sum_leet = md5sum_leet[:index] + char + md5sum_leet[index+1:]

# Get desired password length from user
length = int(input("Enter the desired length of the password: "))

# Generate random password of the desired length
password = ''.join(random.choice(list(md5sum_leet)) for _ in range(length))

print(f"Generated password: {password} (length: {len(password)})")
