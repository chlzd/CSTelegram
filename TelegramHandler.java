package com.example.bubbleapp;

import com.pengrad.telegrambot.TelegramBot;
import com.pengrad.telegrambot.request.SendMessage;
import com.pengrad.telegrambot.response.SendResponse;

public class TelegramHandler extends Thread {

    private String token;
    private long chatId;
    private String str;

    TelegramHandler(String token,long chatId, String str) {
        this.token = token;
        this.chatId = chatId;
        this.str = str;
    }

    @Override
    public void run() {
        TelegramBot bot = new TelegramBot(this.token);
        SendResponse response = bot.execute(new SendMessage(this.chatId, this.str));
    }
}