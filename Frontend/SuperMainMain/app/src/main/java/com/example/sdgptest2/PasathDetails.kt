package com.example.sdgptest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class PasathDetails : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_pasath_details)

        val button = findViewById<android.view.View>(R.id.backbtn)
        button.setOnClickListener {
            val intent = Intent(this, contact_us::class.java)
            startActivity(intent)
        }
    }

}