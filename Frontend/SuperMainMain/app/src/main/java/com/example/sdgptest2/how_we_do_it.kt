package com.example.sdgptest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.ImageButton
import android.widget.TextView
import com.chaquo.python.PyObject
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform

class how_we_do_it : AppCompatActivity() {
    var editTextTextMultiLine: EditText? = null
    var editTextTextMultiLine2: EditText? = null
    var button2: Button? = null
    var true_false: TextView? = null
    override fun onCreate(savedInstanceState: Bundle?) {
//        println("\n\nIntent on How We Do It")
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_how_we_do_it)
        editTextTextMultiLine = findViewById<View>(R.id.editTextTextMultiLine) as EditText
        editTextTextMultiLine2 = findViewById<View>(R.id.editTextTextMultiLine2) as EditText

        true_false = findViewById<View>(R.id.true_false) as TextView

        if (!Python.isStarted()) Python.start(AndroidPlatform(this))
        val py = Python.getInstance()
        val pyobj = py.getModule("main")

        val actionBtn = findViewById<Button>(R.id.urlcheck)
        actionBtn.setOnClickListener(){
            actionBtn.setOnClickListener {
//                simple helloworld for testing
//                val obj = pyobj.callAttr("helloworld", "yasindu").toString()
//                println(obj)

                val obj = pyobj.callAttr("validate_news", editTextTextMultiLine!!.text.toString(), editTextTextMultiLine2!!.text.toString()) as List<PyObject>
                true_false!!.text = "obj.toString()"
                println("\n"+obj)
            }
        }

        val actionBtns = findViewById<Button>(R.id.urlcheck)
        actionBtns.setOnClickListener(){
            actionBtns.setOnClickListener {
                val obj = pyobj.callAttr("validate_news", editTextTextMultiLine!!.text.toString(), editTextTextMultiLine2!!.text.toString()) as List<PyObject>
                true_false!!.text = "obj.toString()"
                println(obj)
            }
        }

        val newNews = findViewById<ImageButton>(R.id.newsnews)
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

//        editTextTextMultiLine!!.setLayerType(View.LAYER_TYPE_HARDWARE, null)
//        editTextTextMultiLine2!!.setLayerType(View.LAYER_TYPE_HARDWARE, null)
//        true_false!!.setLayerType(View.LAYER_TYPE_HARDWARE, null)
//        actionBtn!!.setLayerType(View.LAYER_TYPE_HARDWARE, null)
//        newNews!!.setLayerType(View.LAYER_TYPE_HARDWARE, null)
//        latestNews!!.setLayerType(View.LAYER_TYPE_HARDWARE, null)
//        factCheck!!.setLayerType(View.LAYER_TYPE_HARDWARE, null)
//        contactUs!!.setLayerType(View.LAYER_TYPE_HARDWARE, null)
    }

}