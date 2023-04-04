package com.example.sdgptest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.ImageButton
import com.chaquo.python.Python
import com.chaquo.python.Python.*

class how_we_do_it : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_how_we_do_it)

        val actionBtn = findViewById<Button>(R.id.urlcheck)
        actionBtn.setOnClickListener(){
            println("hi")
        }
        val newNews = findViewById<ImageButton>(R.id.newnews)
        newNews.setOnClickListener(){
            val Intent = Intent(this, MainPage::class.java)
            println("hi")
            startActivity(Intent)
            finish()
        }
        val latestNews = findViewById<ImageButton>(R.id.latestnews)
        latestNews.setOnClickListener(){
            val Intent = Intent(this, MainPage::class.java)
            println("hi")
            startActivity(Intent)
            finish()
        }
        val factCheck = findViewById<ImageButton>(R.id.factcheck)
        factCheck.setOnClickListener(){
            val Intent = Intent(this, how_we_do_it::class.java)
            println("hi")
            startActivity(Intent)
            finish()
        }
        val contactUs = findViewById<ImageButton>(R.id.contact)
        factCheck.setOnClickListener(){
            val Intent = Intent(this, contact_us::class.java)
            println("hi")
            startActivity(Intent)
            finish()
        }
    }

}