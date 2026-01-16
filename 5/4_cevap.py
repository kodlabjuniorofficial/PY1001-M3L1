# Modül-3 Ders-1 Tamamlanmış Öğrenci Çözümü
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start komutu için fonksiyon
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"Merhaba {user_name}! Ben senin emrindeyim. 💂‍♂️")

# /selam komutu için fonksiyon
async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Vay! Bir selam aldım, çok mutlu oldum. Merhaba! 🥳")

if __name__ == '__main__':
    # Bot kurulumu
    app = ApplicationBuilder().token("BURAYA_SİZİN_TOKEN_GELECEK").build()
    
    # Komutların kaydedilmesi
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('selam', say_hello))
    
    print("Sanal Asistan Telegram üzerinden yayında! Komutlar: /start, /selam")
    app.run_polling()