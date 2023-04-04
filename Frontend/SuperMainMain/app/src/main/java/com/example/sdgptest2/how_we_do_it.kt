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
    }

}