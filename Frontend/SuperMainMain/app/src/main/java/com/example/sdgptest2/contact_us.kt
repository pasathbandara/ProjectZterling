package com.example.sdgptest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class contact_us : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_contact_us)

        val  saiDT : Button =findViewById(R.id.person1)
        saiDT.setOnClickListener(){
            val  hh = Intent(this,SaicharanDetails::class.java)
            startActivity(hh)
        }

        val  pasathDT : Button =findViewById(R.id.person4)
        pasathDT.setOnClickListener(){
            val  pasathjk = Intent(this,PasathDetails::class.java)
            startActivity(pasathjk)
        }

        val  chamaljk : Button =findViewById(R.id.person4)
        chamaljk.setOnClickListener(){
            val  chamatdt = Intent(this,ChamalDetails::class.java)
            startActivity(chamatdt)
        }

        val  yasindudt : Button =findViewById(R.id.person4)
        yasindudt.setOnClickListener(){
            val  yasindujk = Intent(this,YasinduDetails::class.java)
            startActivity(yasindujk)
        }

        val  manithjk : Button =findViewById(R.id.person4)
        manithjk.setOnClickListener(){
            val  Manithdt = Intent(this,ManithDetails::class.java)
            startActivity(Manithdt)
        }

    }
}