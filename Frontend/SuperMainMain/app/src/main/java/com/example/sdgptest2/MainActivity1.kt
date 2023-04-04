package com.example.sdgptest2

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.ImageButton
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform

class MainActivity1 : AppCompatActivity() {
    var editTextTextMultiLine: EditText? = null
    var editTextTextMultiLine2: EditText? = null
    var button2: Button? = null
    var true_false: TextView? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_how_we_do_it)
//        editTextTextMultiLine = findViewById<View>(R.id.editTextTextMultiLine) as EditText
//        editTextTextMultiLine2 = findViewById<View>(R.id.editTextTextMultiLine2) as EditText

        val actionBtn = findViewById<Button>(R.id.urlcheck)
        actionBtn.setOnClickListener(){
            println("hi")
        }

        button2 = findViewById<View>(R.id.button2) as Button
        true_false = findViewById<View>(R.id.true_false) as TextView
        if (!Python.isStarted()) Python.start(AndroidPlatform(this))
        val py = Python.getInstance()
        val pyobj = py.getModule("main")

//        final PyObject obj={null};

//        button.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                List<PyObject> obj = (List)pyobj.callAttr("validate_news", editTextTextMultiLine.getText().toString(), editTextTextMultiLine2.getText().toString());
////                PyObject obj2 = pyobj.callAttr("validate_news", editTextTextMultiLine.getText().toString(), editTextTextMultiLine2.getText().toString());
//                true_false.setText(obj.toString());
//                System.out.println(obj);
//            }
//        });

//        button.setOnClickListener(view -> {
//            List<PyObject> obj1 = (List)pyobj.callAttr("validate_news", editTextTextMultiLine.getText().toString(), editTextTextMultiLine2.getText().toString());
////                PyObject obj2 = pyobj.callAttr("validate_news", editTextTextMultiLine.getText().toString(), editTextTextMultiLine2.getText().toString());
//            true_false.setText(obj1.toString());
//            System.out.println(obj1);
//        });

//        button.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                button.setOnClickListener(this);
//                System.out.println("Button Clicked");
//            }
//        });
    }
}