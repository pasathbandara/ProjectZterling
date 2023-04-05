package com.example.sdgptest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class contact_us : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_contact_us)
//picture wise abouts
        val pasathbtn = findViewById<android.view.View>(R.id.pasathbtn)
        pasathbtn.setOnClickListener { val intent = Intent(this, PasathDetails::class.java)
            startActivity(intent)}
        val saichbtn = findViewById<android.view.View>(R.id.saichbtn)
        saichbtn.setOnClickListener { val intent = Intent(this, SaicharanDetails::class.java)
            startActivity(intent)}
        val manithbtn = findViewById<android.view.View>(R.id.manithbtn)
        manithbtn.setOnClickListener { val intent = Intent(this, ManithDetails::class.java)
            startActivity(intent)}
        val yasibtn = findViewById<android.view.View>(R.id.yasibtn)
        yasibtn.setOnClickListener { val intent = Intent(this, YasinduDetails::class.java)
            startActivity(intent)}
        val nikibtn = findViewById<android.view.View>(R.id.nikibtn)
        nikibtn.setOnClickListener { val intent = Intent(this, ChamalDetails::class.java)
            startActivity(intent)}

//toolbar
        val contnews = findViewById<android.view.View>(R.id.contnews)
        contnews.setOnClickListener { val intent = Intent(this, ChamalDetails::class.java)
            startActivity(intent)}
        val contlatestnews = findViewById<android.view.View>(R.id.contlatestnews)
        contnews.setOnClickListener { val intent = Intent(this, ChamalDetails::class.java)
            startActivity(intent)}
        val contfactcheck = findViewById<android.view.View>(R.id.contfactcheck)
        contfactcheck.setOnClickListener { val intent = Intent(this, ChamalDetails::class.java)
            startActivity(intent)}
        val contcont = findViewById<android.view.View>(R.id.contcont)
        contcont.setOnClickListener { val intent = Intent(this, ChamalDetails::class.java)
            startActivity(intent)}
    }
}