package com.example.sdgptest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.Toast

class Splash : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)
        val actionBtn = findViewById<Button>(R.id.readingbtn)
        actionBtn.setOnClickListener() {
            val Intent = Intent(this, MainPage::class.java)
            startActivity(Intent)
            // make a toast message to say welcome
            Toast.makeText(this, "Welcome", Toast.LENGTH_SHORT).show()
            finish()
        }
    }
}