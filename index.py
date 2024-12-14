
import random
import time
def guess_the_song():

    songs = {
        "Malargal Kaettaen": "OK Kanmani - A.R. Rahman 🎶",
        "Pudhu Vellai Mazhai": "Roja - A.R. Rahman 🎶",
        "Enna Solla Pogirai": "Kandukondain Kandukondain - Hariharan 🎤",
        "Vinnaithaandi Varuvaayaa": "Vinnaithaandi Varuvaayaa - A.R. Rahman 🎧",
        "Munbe Vaa": "Sillunu Oru Kaadhal - A.R. Rahman 🎼",
        "Thalli Pogathey": "Achcham Yenbadhu Madamaiyada - A.R. Rahman 🎶",
        "Azhagiya Laila": "Vaaranam Aayiram - Harris Jayaraj 🎶",
        "Vennilave Vennilave": "Minsara Kanavu - A.R. Rahman 🎤",
        "Kaatre Kaatre": "Sundarapandian - G.V. Prakash Kumar 🌟",
        "Kannai Vittu": "Kochadaiiyaan - A.R. Rahman 🎥",
        "Neela Vaanam": "Thulluvadho Ilamai - A.R. Rahman 🌌",
        "Madhurame": "OK Kanmani - A.R. Rahman 🎵",
        "Anbil Avan": "Pariyerum Perumal - Santhosh Narayanan 💖",
        "Suttrum Vizhi": "Suttrum Vizhi - A.R. Rahman 🌟",
        "Poongatrile": "Minsara Kanavu - A.R. Rahman 🌸",
        "Thuli Thuli": "Vaaranam Aayiram - Harris Jayaraj 🎶",
        "Kadhal Rojave": "Roja - A.R. Rahman 💖",
        "Oru Naalil": "Rajanna - Ilaiyaraaja 🎼",
        "Vizhiyile Malarnthidum": "Aasai - A.R. Rahman 🌷",
        "Sundari Neeyum": "Thiruda Thiruda - A.R. Rahman 🌟",
        "Kanavil Kanavil": "Kandukondain Kandukondain - A.R. Rahman 💖",
        "Vaanum Koththum": "Vaanam Koththum - A.R. Rahman 🎤",
        "Sundari Kanal": "Thalapathi - Ilaiyaraaja 🎶"
    }

    score = 0
    rounds = 5
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num}/{rounds} --- 🎶")
        song, artist = random.choice(list(songs.items()))


        all_songs = list(songs.keys())
        choices = random.sample(all_songs, 3)
        choices.append(song)
        random.shuffle(choices)

        print(f"\nYour question: What is the song title? 🎧")
        print(f"Song lyric: \"{song}\" 🎤")
        print("\nOptions:")
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice} 🎶")

        start_time = time.time()
        time_limit = 15
        user_choice = None

        while True:
            if time.time() - start_time > time_limit:
                print("\n⏰ Time's up! ⏰")
                break
            try:
                user_choice = int(input("\nEnter the number of your choice: "))
                if user_choice < 1 or user_choice > 4:
                    print("❌ Invalid choice. Please enter a number between 1 and 4.")
                    continue
                break
            except ValueError:
                print("❌ Invalid input. Please enter a number between 1 and 4.")

        if user_choice and choices[user_choice - 1] == song:
            print("✅ Correct! Well done! 🎉")
            score += 1
        else:
            print(f"❌ Oops! The correct answer is: {song} - {artist} 🎶")

    print(f"\n🎮 Game Over! Your final score is: {score}/{rounds} 🎮")
    if score == rounds:
        print("🌟 Amazing! You scored a perfect score! 🌟")
    elif score >= rounds // 2:
        print("👏 Good job! You have a great knowledge of Tamil melodies! 👏")
    else:
        print("😅 Don't worry, try again and improve your score! 😅")

guess_the_song()
