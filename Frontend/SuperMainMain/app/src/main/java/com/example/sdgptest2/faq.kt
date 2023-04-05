package com.example.sdgptest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class faq : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_faq)

        val faqback = findViewById<android.view.View>(R.id.faqback)
        faqback.setOnClickListener {
            val intent = Intent(this, burgerMenu::class.java)
            startActivity(intent)
        }
    }
}