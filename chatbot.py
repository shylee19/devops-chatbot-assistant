from datetime import datetime

team = ["Shylee", "Sneha", "Akhil", "Chandra"]

for name in team:
    print(f"\n👋 Hello {name}! Let's do your stand-up.")
    yesterday = input("What did you do yesterday? ")
    today = input("What will you do today? ")
    blockers = input("Any blockers or issues? ")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary = f"""
📝 Daily Stand-Up Summary for {name} ({timestamp}):
- Yesterday: {yesterday}
- Today: {today}
- Blockers: {blockers}
"""

    with open("standup_report.txt", "a", encoding="utf-8") as file:
        file.write(summary + "\n")
        file.write("=====================================\n")
