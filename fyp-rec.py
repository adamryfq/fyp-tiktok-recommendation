"""
FYP (For You Page) Recommendation Simulator
--------------------------------------------
An interactive program that simulates TikTok's interest-based
video recommendation system.
"""

import random
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
INTEREST_WEIGHT = 3
OTHER_WEIGHT = 1


def show_welcome_banner():
    print("=" * 42)
    print("        Welcome to TikTok!")
    print("=" * 42)
    print("How to use:")
    print(" - You'll pick an interest to get started")
    print(" - LIKE a video to see more like it")
    print(" - SCROLL to see the next video")
    print(" - CLOSE to end your session")
    print("=" * 42)


def display_interest_menu():
    print("\nWhat are you interested in?")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")


def get_user_interest():
    while True:
        display_interest_menu()
        choice = input(f"Enter your choice (1-{len(CATEGORIES)}): ").strip()
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        choice_num = int(choice)
        if 1 <= choice_num <= len(CATEGORIES):
            return CATEGORIES[choice_num - 1]
        print(f"Please enter a number between 1 and {len(CATEGORIES)}.")


def get_next_action(is_liked):
    like_label = "Unlike" if is_liked else "Like"
    print(f"\n1. {like_label}   2. Scroll   3. Liked videos   4. Close")
    while True:
        choice = input("Choose an action (1-4): ").strip()
        if choice == "1":
            return "like"
        elif choice == "2":
            return "scroll"
        elif choice == "3":
            return "liked_videos"
        elif choice == "4":
            return "close"
        print("Invalid input. Please enter 1, 2, 3, or 4.")


def build_initial_queue(interest):
    matches = [v for v in VIDEOS if v["category"] == interest]
    matches.sort(key=lambda v: v["likes"], reverse=True)
    return matches


def get_interests(original_interest, liked_videos):
    interests = {original_interest}
    for video in liked_videos:
        interests.add(video["category"])
    return interests


def get_next_video(queue, interests):
    if queue:
        return queue.pop(0)

    weights = []
    for video in VIDEOS:
        if video["category"] in interests:
            weights.append(INTEREST_WEIGHT)
        else:
            weights.append(OTHER_WEIGHT)
    return random.choices(VIDEOS, weights=weights, k=1)[0]


def display_video(video):
    print("\nNow watching...")
    time.sleep(1)
    print(f"Title:    {video['title']}")
    print(f"Category: {video['category']}")
    print(f"Likes:    {video['likes']:,}")


def toggle_like(video, liked_videos):
    if video in liked_videos:
        liked_videos.remove(video)
        video["likes"] -= 1
        print(f"You unliked \"{video['title']}\". Now at {video['likes']:,} likes.")
    else:
        liked_videos.append(video)
        video["likes"] += 1
        print(f"You liked \"{video['title']}\"! Now at {video['likes']:,} likes.")


def report_interest_changes(before, after):
    for category in sorted(after - before):
        print(f"'{category}' was added to your interests.")
    for category in sorted(before - after):
        print(f"'{category}' was removed from your interests.")


def display_liked_list(liked_videos):
    print("\n--- Your liked videos ---")
    for number, video in enumerate(liked_videos, start=1):
        print(f"{number}. {video['title']} ({video['category']})")


def get_liked_video_choice(total):
    while True:
        choice = input(f"Enter a number (1-{total}) to watch it, or 0 to go back to your feed: ").strip()
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        choice_num = int(choice)
        if 0 <= choice_num <= total:
            return choice_num
        print(f"Please enter a number between 0 and {total}.")


def get_liked_page_action():
    print("\n1. Scroll   2. Back to liked list")
    while True:
        choice = input("Choose an action (1-2): ").strip()
        if choice == "1":
            return "scroll"
        elif choice == "2":
            return "back"
        print("Invalid input. Please enter 1 or 2.")


def watch_liked_videos(liked_videos, start_index):
    for index in range(start_index, len(liked_videos)):
        display_video(liked_videos[index])
        if get_liked_page_action() == "back":
            return
    print("\nYou've reached the end of your liked videos.")


def show_liked_videos_page(liked_videos):
    while True:
        if not liked_videos:
            print("\nYou haven't liked any videos yet.")
            return
        display_liked_list(liked_videos)
        choice = get_liked_video_choice(len(liked_videos))
        if choice == 0:
            return
        watch_liked_videos(liked_videos, choice - 1)


def main():
    show_welcome_banner()
    interest = get_user_interest()
    queue = build_initial_queue(interest)
    liked_videos = []
    current_video = get_next_video(queue, get_interests(interest, liked_videos))

    while True:
        display_video(current_video)
        action = get_next_action(current_video in liked_videos)
        if action == "like":
            interests_before = get_interests(interest, liked_videos)
            toggle_like(current_video, liked_videos)
            interests_after = get_interests(interest, liked_videos)
            report_interest_changes(interests_before, interests_after)
        elif action == "scroll":
            interests = get_interests(interest, liked_videos)
            current_video = get_next_video(queue, interests)
        elif action == "liked_videos":
            show_liked_videos_page(liked_videos)
        elif action == "close":
            break

    print("\n=== Session ended ===")
    print("Thanks for using the FYP simulator!")


if __name__ == "__main__":
    main()