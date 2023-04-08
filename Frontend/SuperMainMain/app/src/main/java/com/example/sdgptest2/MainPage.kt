package com.example.sdgptest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageButton
import android.widget.Toast

class MainPage : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val burgmenu = findViewById<ImageButton>(R.id.burgmenu)
        burgmenu.setOnClickListener() {
            val Intent = Intent(this, BurgerMenu::class.java)
            startActivity(Intent)
            finish()
        }
        // Handle clicks on other buttons
        val contnews = findViewById<android.view.View>(R.id.imageButton3)
        contnews.setOnClickListener {
            val intent = Intent(this, MainPage::class.java)
            startActivity(intent)
            Toast.makeText(
                applicationContext, "Already In the Main Page", Toast.LENGTH_SHORT
            ).show()
        }
        val contlatestnews = findViewById<android.view.View>(R.id.imageButton8)
        contlatestnews.setOnClickListener {
            val intent = Intent(this, AllNews::class.java)
            startActivity(intent)
            Toast.makeText(
                applicationContext, "Going to the All News Page", Toast.LENGTH_SHORT
            ).show()
        }
        val contfactcheck = findViewById<android.view.View>(R.id.imageButton2)
        contfactcheck.setOnClickListener {
            val intent = Intent(this, how_we_do_it::class.java)
            startActivity(intent)
            Toast.makeText(
                applicationContext, "Going to the Fact Check Page", Toast.LENGTH_SHORT
            ).show()
        }
        val contcont = findViewById<android.view.View>(R.id.imageButton9)
        contcont.setOnClickListener {
            val intent = Intent(this, contact_us::class.java)
            startActivity(intent)
            Toast.makeText(
                applicationContext, "Going to the Contact Us Page", Toast.LENGTH_SHORT
            ).show()
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