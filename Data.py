from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
سلاااااام {}
به ربات من خوش اومدی🖐

من میتونم در مورد pdf به شما کمک کنم یا مثلا تصاویر رو به pdf تبدیل کنم یا...

برای دیدن ویژگی ها از /help استفاده کنید.

فقط برای شروع یک PDF (یا یک تصویر) ارسال کنید.🐥

🏝Coded by : @OPStxt
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("کانال من✨", url="https://t.me/+zi81BsXHmT42YjQx")],
        [
            InlineKeyboardButton("نحوه استفاده❔", callback_data="help"),
            
        ],
       
  ]
    # Help Message
    HELP = """
**Usage**

1) Just send a PDF to do stuff on it

2) Send images to convert to PDFs

**Functions**

1) Rotate PDF Pages

2) Merge PDFs

3) Encrypt PDFs

4) Decrypt PDFs

5) Convert Images to PDF
