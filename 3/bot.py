from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# asenkron (async) bir fonksiyon tanımlıyoruz
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 'await' kullanarak botun mesajı göndermesini bekliyoruz
    # update.message.reply_text -> Garsonun yemeği masaya servis etmesi gibidir.
    await update.message.reply_text("Merhaba! Ben senin yeni botunum. 🤖")

if __name__ == '__main__':
    # Botun fabrikasını kuruyoruz
    token = "BURAYA_TOKEN_GELECEK"
    app = ApplicationBuilder().token(token).build()
    
    # Komut Dinleyicisi (Handler) ekliyoruz: /start yazınca 'start' fonksiyonu çalışsın
    app.add_handler(CommandHandler('start', start))
    
    print("Bot şu an Telegram sunucularını dinliyor... Test edebilirsiniz!")
    app.run_polling()