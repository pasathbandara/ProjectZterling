package com.example.projectz

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import androidx.core.content.ContextCompat.startActivity

class Splash : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)
        val actionBtn = findViewById<Button>(R.id.readingbtn)
        actionBtn.setOnClickListener() {
            val intent = Intent(this, MainPage::class.java)
            startActivity(intent)
            finish()
        }
    }
}