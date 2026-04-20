import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Token depuis variable d'environnement (Render) ou valeur par défaut (local)
TOKEN = os.environ.get("BOT_TOKEN", "8713104272:AAGuu-HE3v6_yIIL9dbIf7s49SpVj4oRmgg")

# MENU PRINCIPAL
def main_menu():
    keyboard = [
        [InlineKeyboardButton("📲 Accéder à la mini app",
            web_app=WebAppInfo(url="https://69e63efbc84e202d194dccb0--dainty-marzipan-b99def.netlify.app/")
        )],
        [InlineKeyboardButton("🛟 Support", callback_data="support")],
        [InlineKeyboardButton("📢 Canal", url="https://t.me/rsqcoffe")]
    ]
    return InlineKeyboardMarkup(keyboard)

# MENU SUPPORT
def support_menu():
    keyboard = [
        [InlineKeyboardButton("👻 Snapchat", url="https://www.snapchat.com/add/zerorisque6.2")],
        [InlineKeyboardButton("🔙 Retour", callback_data="menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=open("logo1.png", "rb"),
        caption="""🔥 Bienvenue chez Le Risque 

🔓 Nous sommes ouvert de 12H à 00H
🟢 Sur place sécurisé 
💯 Qualité certifié
📲 Ouvrez la mini-application et passer commande ! 
📲 Ajoutez nous sur snapchat 👻""",
        reply_markup=main_menu(),
        parse_mode="HTML"
    )

# GESTION DES CLICS
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "support":
        await query.edit_message_caption(
            caption="""🛟 Support

Contacte-nous rapidement via Snapchat 👻
""",
            reply_markup=support_menu(),
            parse_mode="HTML"
        )

    elif query.data == "menu":
        await query.edit_message_caption(
            caption="""🔥 Bienvenue chez Le Risque 

🔓 Nous sommes ouvert de 12H à 00H
🟢 Sur place sécurisé 
💯 Qualité certifié
📲 Ouvrez la mini-application et passer commande ! 
📲 Ajoutez nous sur snapchat 👻""",
            reply_markup=main_menu(),
            parse_mode="HTML"
        )

# 🔹 LANCEMENT
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
