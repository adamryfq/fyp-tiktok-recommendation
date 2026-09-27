"""
FYP (For You Page) Recommendation Simulator
--------------------------------------------
An interactive program that simulates TikTok's interest-based
video recommendation system.
"""

import time

VIDEOS = [
    {"title": "5-Minute Pasta Hack", "category": "Cooking", "likes": 12400},
    {"title": "Midnight Snack Ideas", "category": "Cooking", "likes": 8700},
    {"title": "One-Pot Ramen Recipe", "category": "Cooking", "likes": 15600},
    {"title": "Try Not To Laugh Challenge", "category": "Comedy", "likes": 20100},
    {"title": "Office Prank Gone Wrong", "category": "Comedy", "likes": 9800},
    {"title": "Roommate Fails Compilation", "category": "Comedy", "likes": 17300},
    {"title": "Learn This Viral Dance", "category": "Dance", "likes": 25600},
    {"title": "Beginner Dance Tutorial", "category": "Dance", "likes": 11200},
    {"title": "Dance Trend Remix", "category": "Dance", "likes": 19800},
]
CATEGORIES = ["Cooking", "Comedy", "Dance"]


def display_menu():
    print("\nWhat are you interested in?")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")


def get_user_interest():
    while True:
        display_menu()
        choice = input(f"Enter your choice (1-{len(CATEGORIES)}): ").strip()
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        choice_num = int(choice)
        if 1 <= choice_num <= len(CATEGORIES):
            return CATEGORIES[choice_num - 1]
        print(f"Please enter a number between 1 and {len(CATEGORIES)}.")


def get_recommendations(interest):
    matches = [video for video in VIDEOS if video["category"] == interest]
    matches.sort(key=lambda video: video["likes"], reverse=True)
    return matches


def display_video(video):
    print("\nNow playing...")
    time.sleep(1)
    print(f"Title:    {video['title']}")
    print(f"Category: {video['category']}")
    print(f"Likes:    {video['likes']:,}")


def display_recommendations(interest, recommendations):
    print(f"\n--- Recommended for you: {interest} ---")
    for video in recommendations:
        display_video(video)


def main():
    print("=== Welcome to the FYP Recommendation Simulator ===")
    interest = get_user_interest()
    recommendations = get_recommendations(interest)
    display_recommendations(interest, recommendations)
    print("\nThanks for watching! (End of simulation)")


if __name__ == "__main__":
    main()