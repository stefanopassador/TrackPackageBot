CREATE TABLE IF NOT EXISTS telegram_message_received (
    message_id BIGINT PRIMARY KEY,
    from_id BIGINT,
    from_is_bot BOOLEAN,
    from_first_name TEXT,
    from_last_name TEXT,
    from_username TEXT,
    from_language_code TEXT,
    chat_id BIGINT,
    chat_first_name TEXT,
    chat_last_name TEXT,
    chat_username TEXT,
    chat_type TEXT,
    date BIGINT,
    text TEXT
);