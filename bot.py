import random
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, CommandHandler, InlineQueryHandler
from telegram.error import BadRequest

TOKEN = '7503744644:AAEnSaFuHdPwuav0SmJV4CW8jV4qVio84ps'  # Замените на токен вашего бота

# Список вопросов с черным юмором и соответствующие им ответы
questions_and_responses = {
    "Сколько раз я дрочил сегодня?": [
        "3-4 раза",
        "5-6 раз",
        "Ни разу, ну ты и лентяй!",
        "Сегодня? Уже 10 раз!",
        "Слишком много, чтобы считать"
    ],
    "Сколько еще дней я проживу?": [
        "Ещё пару дней, и ты станешь бессмертным!",
        "Учитывая твою удачу, не больше недели.",
        "Всё зависит от твоего соседа по комнате.",
        "Пока не надоест твоему коту.",
        "Тебе лучше не знать..."
    ],
    "Почему я такой неудачник?": [
        "Неудачники не задают таких вопросов.",
        "Ты просто неудачливый гений.",
        "Кто-то должен быть, почему не ты?",
        "Просто плохой день, или жизнь.",
        "Потому что ты веришь в судьбу."
    ],
    "Что мне сделать, чтобы мои соседи съехали?": [
        "Попробуй громко слушать металл по ночам.",
        "Заведи 10 кошек и не убирай за ними.",
        "Организуй ночные вечеринки каждый день.",
        "Начни курить кальян на балконе.",
        "Стань лучшим другом их детей."
    ],
    "Как мне избежать налогов?": [
        "Спрячься в офшорах и надейся на лучшее.",
        "Стань невидимым для налоговой.",
        "Придумай, что ты монах.",
        "Переходи на бартер.",
        "Просто не плати и смотри, что будет."
    ]
}

# Список вопросов с упоминанием участников чата
questions_with_mentions = {
    "Кто сегодня самый ленивый?": [
        "Определенно @{username}!",
        "Сегодня это @{username}.",
        "Кажется, @{username} взял выходной.",
        "Без сомнений, это @{username}.",
        "Все указывает на @{username}."
    ],
    "Кто больше всех треплет нервы?": [
        "Конечно, это @{username}.",
        "Больше всех раздражает @{username}.",
        "Сегодня это @{username}.",
        "Все указывает на @{username}.",
        "Без сомнений, это @{username}."
    ],
    "Кто больше всех сплетничает?": [
        "Определенно, это @{username}.",
        "Сплетник дня - @{username}.",
        "Все указывает на @{username}.",
        "Сегодня это @{username}.",
        "Без сомнений, сплетник - @{username}."
    ]
}

# Обработка инлайн-запросов
async def inlinequery(update: Update, context) -> None:
    query = update.inline_query.query.lower()
    results = []

    # Получаем администраторов чата, если это группа или супергруппа
    admin_usernames = []
    try:
        if update.inline_query.chat_type in ['group', 'supergroup']:
            chat_id = update.inline_query.from_user.id
            chat_admins = await context.bot.get_chat_administrators(chat_id)
            admin_usernames = [admin.user.username for admin in chat_admins if admin.user.username]
    except BadRequest as e:
        print(f"Error getting chat administrators: {e}")

    for i, (question, responses) in enumerate(questions_and_responses.items()):
        if query in question.lower() or not query:
            random_response = random.choice(responses)
            results.append(
                InlineQueryResultArticle(
                    id=f"q{i}",
                    title=question,
                    input_message_content=InputTextMessageContent(
                        f"Вы выбрали вопрос: {question}\nОтвет: {random_response}"
                    ),
                    description=question
                )
            )

    for i, (question, responses) in enumerate(questions_with_mentions.items()):
        if (query in question.lower() or not query) and admin_usernames:
            random_user = random.choice(admin_usernames)
            random_response = random.choice(responses).replace("{username}", random_user)
            results.append(
                InlineQueryResultArticle(
                    id=f"m{i}",
                    title=question,
                    input_message_content=InputTextMessageContent(
                        f"Вы выбрали вопрос: {question}\nОтвет: {random_response}"
                    ),
                    description=question
                )
            )

    await update.inline_query.answer(results, cache_time=0)

# Обработка команды /start
async def start(update: Update, context) -> None:
    await update.message.reply_text("Привет! Используй инлайн-запросы, чтобы задать вопросы и получить ответы.")

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(InlineQueryHandler(inlinequery))

    application.run_polling()

if __name__ == '__main__':
    main()