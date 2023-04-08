// Package declaration
package com.example.sdgptest2

// Import statements
import android.content.Context
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
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Body
import retrofit2.http.POST
import java.net.NoRouteToHostException

// Class declaration for "how_we_do_it" activity
class how_we_do_it : AppCompatActivity() {
    // Variable declarations for UI components
    var editTextTextMultiLine: EditText? = null
    var editTextTextMultiLine2: EditText? = null
    var button2: Button? = null
    var true_false: TextView? = null

    // Retrofit setup
    val retrofit = Retrofit.Builder()
        .baseUrl("http://192.168.1.2:5000") // Replace <your_ip_address> with your computer's IP address
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    val api = retrofit.create(NewsApi::class.java)

    // onCreate() method
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Set content view for activity
        setContentView(R.layout.activity_how_we_do_it)

        // Initialize UI components
        editTextTextMultiLine = findViewById<View>(R.id.editTextTextMultiLine) as EditText
        editTextTextMultiLine2 = findViewById<View>(R.id.editTextTextMultiLine2) as EditText

        true_false = findViewById<View>(R.id.true_false) as TextView

        // Handle button click
        val actionBtn = findViewById<Button>(R.id.urlcheck)
        actionBtn.setOnClickListener() {
            // If the Device is connected to the internet
            try {
                println(
                    "Device is connected to the Internet. " +
                            "\nApplication Functionalities will be done using Flask API"
                )
                val url = editTextTextMultiLine!!.text.toString()
                val news = editTextTextMultiLine2!!.text.toString()

                // Prepare data for API request
                val data = mapOf("url" to url, "news" to news)

                // Send API request
                api.validateNews(data).enqueue(object : Callback<Map<String, Any>> {
                    override fun onResponse(
                        call: Call<Map<String, Any>>,
                        response: Response<Map<String, Any>>
                    ) {
                        if (response.isSuccessful) {
                            // Handle successful response
                            println("Response Generated")
                            val result = response.body()!!["result"] as String
                            val reliabilityRating =
                                response.body()!!["reliability_rating"] as Double
                            true_false!!.text = "$result: $reliabilityRating/5)"
                            println(result + " " + reliabilityRating)
                        } else {
                            println("Response Unsuccessful")
                        }
                    }

                    override fun onFailure(call: Call<Map<String, Any>>, t: Throwable) {
                        println("Connection Failed \n${t.message}")
                    }
                })
            }
            // If the Device is not connected to the internet
            catch (e: NoRouteToHostException) {
                startChaqoupyFramework(this)
            }
            // If there is any other exception
            catch (e: java.lang.Exception) {
                print(e.stackTrace)
                startChaqoupyFramework(this)
            }
        }

        // Handle clicks on other buttons
        val newNews = findViewById<ImageButton>(R.id.newsnews)
        newNews.setOnClickListener() {
            val Intent = Intent(this, MainPage::class.java)
            println("hi")
            startActivity(Intent)
            finish()
        }
        val latestNews = findViewById<ImageButton>(R.id.latestnews)
        latestNews.setOnClickListener() {
            val Intent = Intent(this, MainPage::class.java)
            println("hi")
            startActivity(Intent)
            finish()
        }
        val factCheck = findViewById<ImageButton>(R.id.factcheck)
        factCheck.setOnClickListener() {
            val Intent = Intent(this, how_we_do_it::class.java)
            println("hi")
            startActivity(Intent)
            finish()
        }
        val contactUs = findViewById<ImageButton>(R.id.contact)
        factCheck.setOnClickListener() {
            val Intent = Intent(this, contact_us::class.java)
            println("hi")
            startActivity(Intent)
            finish()
        }
    }

    //interface for the News API used in the SDGP Test 2 application.
    interface NewsApi {
        @POST("/validate_news")
        fun validateNews(@Body data: Map<String, String>): Call<Map<String, Any>>
    }

    /*
    ----------------------------- THE BELOW CODE IS TO BE USED WHEN THE USER IS NOT CONNECTED TO INTERNET---------------------------------------------------
    */
    fun startChaqoupyFramework(context: Context) {
        println(
            "Device isn't connected to the Internet. " +
                    "\nApplication Functionalities will be done using chaqoupy framework" +
                    "\nYou might experience crashes and bugs"
        )
        if (!Python.isStarted()) Python.start(AndroidPlatform(context))

        val py = Python.getInstance()

        val actionBtn = findViewById<Button>(R.id.urlcheck)
        actionBtn.setOnClickListener() {
            actionBtn.setOnClickListener {
                /*  To Test A Function - Offline Mode
                simple function for testing
                val pyobj = py.getModule("hello_user")
                val obj = pyobj.callAttr("helloworld").toString()
                true_false!!.text = obj
                println(obj)
                 */

                val pyobj = py.getModule("main")
                val obj = pyobj.callAttr(
                    "validate_news",
                    editTextTextMultiLine!!.text.toString(),
                    editTextTextMultiLine2!!.text.toString()
                ) as List<PyObject>
                true_false!!.text = "obj.toString()"
                println("\n" + obj)
            }
        }
    }
}