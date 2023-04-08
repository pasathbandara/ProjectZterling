package com.example.sdgptest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast

class contact_us : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_contact_us)
//picture wise abouts
        val pasathbtn = findViewById<android.view.View>(R.id.pasathbtn)
        pasathbtn.setOnClickListener {
            val intent = Intent(this, PasathDetails::class.java)
            startActivity(intent)
        }
        val saichbtn = findViewById<android.view.View>(R.id.saichbtn)
        saichbtn.setOnClickListener {
            val intent = Intent(this, SaicharanDetails::class.java)
            startActivity(intent)
        }
        val manithbtn = findViewById<android.view.View>(R.id.manithbtn)
        manithbtn.setOnClickListener {
            val intent = Intent(this, ManithDetails::class.java)
            startActivity(intent)
        }
        val yasibtn = findViewById<android.view.View>(R.id.yasibtn)
        yasibtn.setOnClickListener {
            val intent = Intent(this, YasinduDetails::class.java)
            startActivity(intent)
        }
        val nikibtn = findViewById<android.view.View>(R.id.nikibtn)
        nikibtn.setOnClickListener {
            val intent = Intent(this, ChamalDetails::class.java)
            startActivity(intent)
        }

//toolbar
        val contnews = findViewById<android.view.View>(R.id.contnews)
        contnews.setOnClickListener {
            val intent = Intent(this, MainPage::class.java)
            startActivity(intent)
            Toast.makeText(
                applicationContext, "Going to the Main Page", Toast.LENGTH_SHORT
            ).show()
        }
        val contlatestnews = findViewById<android.view.View>(R.id.contlatestnews)
        contlatestnews.setOnClickListener {
            val intent = Intent(this, AllNews::class.java)
            startActivity(intent)
            Toast.makeText(
                applicationContext, "Going to the All News Page", Toast.LENGTH_SHORT
            ).show()
        }
        val contfactcheck = findViewById<android.view.View>(R.id.contfactcheck)
        contfactcheck.setOnClickListener {
            val intent = Intent(this, how_we_do_it::class.java)
            startActivity(intent)
            Toast.makeText(
                applicationContext, "Going to Fact Check Page", Toast.LENGTH_SHORT
            ).show()
        }
        val contcont = findViewById<android.view.View>(R.id.contcont)
        contcont.setOnClickListener {
            val intent = Intent(this, contact_us::class.java)
            startActivity(intent)
            Toast.makeText(
                applicationContext, "Already in the Contact Us", Toast.LENGTH_SHORT
            ).show()
        }
    }
}