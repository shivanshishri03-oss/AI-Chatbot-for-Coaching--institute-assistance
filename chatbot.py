def get_response(user_input):
    user_input = user_input.lower().strip()

    # ---------------- MENU ----------------
    if user_input in ["menu", "hi", "hello", "hii", "start"]:
        return (
            "👋 Welcome to Bright Future Coaching Institute\n\n"
            "📚 Please choose an option:\n"
            "1️⃣ JEE Course\n"
            "2️⃣ NEET Course\n"
            "3️⃣ UPSC Course\n"
            "4️⃣ Fees Details\n"
            "5️⃣ Admission Process\n"
            "6️⃣ Location\n"
            "7️⃣ Contact Number\n\n"
            "👉 Reply with number (1-7)"
        )

    # ---------------- OPTIONS ----------------
    elif user_input == "1":
        return "📘 JEE Course:\nDuration: 1 year\nFee: ₹50,000\nIncludes test series & study material."

    elif user_input == "2":
        return "🧪 NEET Course:\nDuration: 1 year\nFee: ₹50,000."

    elif user_input == "3":
        return "🏛 UPSC Course:\nDuration: 1.5 years\nFee: ₹40,000."

    elif user_input == "4":
        return (
            "💰 Fees Details:\n"
            "JEE: ₹50,000\n"
            "NEET: ₹50,000\n"
            "UPSC: ₹40,000"
        )

    elif user_input == "5":
        return "📝 Admission Process:\nFill form → Pay fees → Start classes."

    elif user_input == "6":
        return (
            "📍 Bright Future Coaching Institute\n"
            "2nd Floor, Shyam Plaza, Near Bus Stand,\n"
            "Indore, Madhya Pradesh."
        )

    elif user_input == "7":
        return "📞 Call us at: +91-9876543210"

    # ---------------- FALLBACK ----------------
    else:
        return (
            "❌ Sorry, I didn't understand.\n\n"
            "👉 Type *menu* to see options."
        )