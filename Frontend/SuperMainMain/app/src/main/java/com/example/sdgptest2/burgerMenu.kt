package com.example.sdgptest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class burgerMenu : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_burger_menu)

        val menulatestnews = findViewById<android.view.View>(R.id.menulatestnews)
        menulatestnews.setOnClickListener {
            val intent = Intent(this, MainPage::class.java)
            startActivity(intent)
        }

        val menufactcheck = findViewById<android.view.View>(R.id.menufactcheck)
        menufactcheck.setOnClickListener {
            val intent = Intent(this, how_we_do_it::class.java)
            startActivity(intent)
        }

        val menucontactus = findViewById<android.view.View>(R.id.menucontactus)
        menucontactus.setOnClickListener {
            val intent = Intent(this, contact_us::class.java)
            startActivity(intent)
        }


    }
}