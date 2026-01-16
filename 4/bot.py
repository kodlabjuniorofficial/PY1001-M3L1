from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. GÖREV: start fonksiyonunu kişiselleştir
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Kullanıcı adını değişken olarak al
    user_name = update.effective_user.first_name
    # Mesajın içine ismi yerleştir ve bir emoji ekle
    await update.message.reply_text(f"Hoş geldin {user_name}! ✨")

# 2. GÖREV: 'say_hello' adında yeni bir asenkron fonksiyon oluştur
# Bu fonksiyon /selam komutuna cevap verecek
async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Buraya kendi özel karşılama mesajını yaz
    await update.message.reply_text("Sana da selam dostum! Bugün harika bir gün. 🚀")

if __name__ == '__main__':
    # 3. GÖREV: Kendi Token'ını gir
    my_token = "BURAYA_TOKEN_GELECEK"
    app = ApplicationBuilder().token(my_token).build()
    
    # Komutları kaydet
    app.add_handler(CommandHandler('start', start))
    
    # 4. GÖREV: /selam komutunu 'CommandHandler' ile ekle
    app.add_handler(CommandHandler('selam', say_hello))
    
    print("Bot çalışıyor... Telegram'dan kontrol et!")
    app.run_polling()