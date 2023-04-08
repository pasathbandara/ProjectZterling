package com.example.sdgptest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageButton

class MainPage : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val burgmenu = findViewById<ImageButton>(R.id.burgmenu)
        burgmenu.setOnClickListener(){
            val Intent = Intent(this, burgerMenu::class.java)
            startActivity(Intent)
            finish()
        }

        val fakeNewsBtn = findViewById<android.view.View>(R.id.textView22)
        fakeNewsBtn.setOnClickListener {
            val intent = Intent(this, FakeNews::class.java)
            startActivity(intent)
        }

        val realNewsBtn = findViewById<android.view.View>(R.id.textView23)
        realNewsBtn.setOnClickListener {
            val intent = Intent(this, TrueNews::class.java)
            startActivity(intent)
        }

        val allNewsBtn = findViewById<android.view.View>(R.id.textView24)
        allNewsBtn.setOnClickListener {
            val intent = Intent(this, AllNews::class.java)
            startActivity(intent)
        }
    }
}