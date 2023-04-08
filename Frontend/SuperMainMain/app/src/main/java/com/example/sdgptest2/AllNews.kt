package com.example.sdgptest2

import android.Manifest
import android.content.Context
import android.content.pm.PackageManager
import android.os.Bundle
import android.os.Environment
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.opencsv.CSVReader
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import java.io.FileReader
import com.squareup.moshi.Json
import com.squareup.moshi.JsonClass

class AllNews : AppCompatActivity() {

    private lateinit var textView: TextView

    // Retrofit setup
    val retrofit = Retrofit.Builder()
        .baseUrl("http://192.168.1.2:5000") // Replace <your_ip_address> with your computer's IP address
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    // Create Retrofit Service
    val newsApiService = retrofit.create(NewsService::class.java)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_all_news)
        textView = findViewById(R.id.allnewstextview) as TextView

        try {
            // Call the API
            newsApiService.getNews().enqueue(object : Callback<List<News>> {
                override fun onResponse(call: Call<List<News>>, response: Response<List<News>>) {
                    if (response.isSuccessful) {
                        val newsList = response.body()

                        // Display the news in the TextView
                        textView.text = newsList?.joinToString(separator = "\n\n") {
                            "${it.title}\n${it.text}\n${it.domain}\n${it.validity}\n${it.rating}"
                        }
                    }
                }

                override fun onFailure(call: Call<List<News>>, t: Throwable) {
                    textView.text = "Error: ${t.message}"

                }
            })
        }
        // Read Local Database (Offline Mode)
        catch (e: Exception) {
            println(e.printStackTrace())
            offlineRetrieveAll(this)
        }

    }

    private fun displayAllDB() {
        // Retrieve the fake news list
        val allDBList = retrieveAllDB()

        // Add the content of the fake news list to the textview
        for (news in allDBList) {
            val title = news[0]
            val text = news[1]
            val domain = news[2]
            val validity = news[3]
            val identifier = news[4]
            val rating = news[5]
            textView.append("$title\n$text\n$domain\n$validity\n$identifier\n$rating\n\n")
        }
    }

    private fun retrieveAllDB(): List<Array<String>> {
        val allDBList = mutableListOf<Array<String>>()

        try {
            val path = Environment.getExternalStorageDirectory().path + "/All_DB.csv"
            val reader = CSVReader(FileReader(path))
            // Skip the heading using the readNext function:
            reader.readNext()
            var row: Array<String>?
            while (reader.readNext().also { row = it } != null) {
                allDBList.add(row!!)
            }
        } catch (e: Exception) {
            e.printStackTrace()
            textView.text = "Error retrieving data from file"
        }

        if (allDBList.isEmpty()) {
            textView.text = "File is empty"
        }

        return allDBList
    }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)

        if (requestCode == PERMISSION_REQUEST_CODE && grantResults.isNotEmpty() &&
            grantResults[0] == PackageManager.PERMISSION_GRANTED
        ) {
            displayAllDB()
        }
    }

    companion object {
        private const val PERMISSION_REQUEST_CODE = 1
    }

    fun offlineRetrieveAll(context: Context) {
        println("Reading from local database ")
        // Request READ_EXTERNAL_STORAGE permission if not already granted
        if (ContextCompat.checkSelfPermission(
                this,
                Manifest.permission.READ_EXTERNAL_STORAGE
            ) != PackageManager.PERMISSION_GRANTED
        ) {
            ActivityCompat.requestPermissions(
                this,
                arrayOf(Manifest.permission.READ_EXTERNAL_STORAGE),
                PERMISSION_REQUEST_CODE
            )
        } else {
            displayAllDB()
        }
    }

    @JsonClass(generateAdapter = true)
    data class News(
        @Json(name = "title") val title: String,
        @Json(name = "text") val text: String,
        @Json(name = "domain") val domain: String,
        @Json(name = "validity") val validity: String,
        @Json(name = "rating") val rating: String
    )

    interface NewsService {
        @GET("/all_news")
        fun getNews(): Call<List<News>>
    }

}