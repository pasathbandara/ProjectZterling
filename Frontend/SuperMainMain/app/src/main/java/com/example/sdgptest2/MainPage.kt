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
            println("hi")
            startActivity(Intent)
            finish()
        }
    }
}