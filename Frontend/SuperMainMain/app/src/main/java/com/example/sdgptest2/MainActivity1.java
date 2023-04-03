package com.example.sdgptest2;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

import java.util.List;

public class MainActivity1 extends AppCompatActivity {

    EditText editTextTextMultiLine, editTextTextMultiLine2;
    Button button, button2;
    TextView true_false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_how_we_do_it);

        editTextTextMultiLine = (EditText)findViewById(R.id.editTextTextMultiLine);
        editTextTextMultiLine2 = (EditText)findViewById(R.id.editTextTextMultiLine2);
        button = (Button)findViewById(R.id.button);
        button2 = (Button)findViewById(R.id.button2);
        true_false = (TextView)findViewById(R.id.true_false);



        if( ! Python. isStarted( ) )
            Python. start(new AndroidPlatform(this));

        Python py = Python.getInstance();
        final PyObject pyobj = py.getModule("main");

//        final PyObject obj={null};

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                List<PyObject> obj = (List)pyobj.callAttr("validate_news", editTextTextMultiLine.getText().toString(), editTextTextMultiLine2.getText().toString());
//                PyObject obj2 = pyobj.callAttr("validate_news", editTextTextMultiLine.getText().toString(), editTextTextMultiLine2.getText().toString());
                true_false.setText(obj.toString());

            }
        });
    }
}
