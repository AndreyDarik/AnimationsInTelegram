from pyrogram import Client, filters
import asyncio

api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"

app = Client("account", api_id, api_hash)

@app.on_message(filters.regex("YOUR_SPECIFIC_WORD"))
async def loading_bar(client, message):
    loading_frames = [
        "[                    ] 0%",
        "[█                 ] 10%",
        "[██                ] 20%",
        "[███               ] 30%",
        "[████              ] 40%",
        "[█████             ] 50%",
        "[██████            ] 60%",
        "[███████           ] 70%",
        "[████████          ] 80%",
        "[█████████         ] 90%",
        "[██████████        ] 100%",
        "Загрузка завершена! 🚀"
    ]

    for frame in loading_frames:
        try:
            await message.edit_text(frame)
            await asyncio.sleep(0.3)  # Задержка между кадрами
        except Exception as e:
            print(f"Ошибка: {e}")
            break

app.run()