package com.example.sdgptest2

import android.Manifest
import android.content.Context
import android.content.pm.PackageManager
import android.os.Build
import android.os.Bundle
import android.os.Environment
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.opencsv.CSVReader
import com.squareup.moshi.Json
import com.squareup.moshi.JsonClass
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import java.io.FileReader

class TrueNews : AppCompatActivity() {
    private lateinit var textView: TextView

    // Retrofit setup
    val retrofit = Retrofit.Builder()
        .baseUrl("http://192.168.8.102:5000") // Replace <your_ip_address> with your computer's IP address
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    val newsApiService = retrofit.create(TrueNews.TrueNewsService::class.java)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_true_news)
        textView = findViewById(R.id.truenewstextview)

        try {
            // Call the API
            newsApiService.getNews().enqueue(object : Callback<List<AllNews.News>> {
                override fun onResponse(
                    call: Call<List<AllNews.News>>,
                    response: Response<List<AllNews.News>>
                ) {
                    if (response.isSuccessful) {
                        val newsList = response.body()

                        // Display the news in the TextView
                        textView.text = newsList?.joinToString(separator = "\n\n\n\n") {
                            "-TOPIC-\n\n ${it.title}\n\n${it.text}\n\nDomain: ${it.domain}\n\nValidity: ${it.validity}\n\nRating: ${it.rating}"
                        }
                    }
                }

                override fun onFailure(call: Call<List<AllNews.News>>, t: Throwable) {
                    println("Error: \n${t.message}")
                }
            })
        }
        // Read Local Database (Offline Mode)
        catch (e: Exception) {
            println(e.printStackTrace())
            offlineRetrieveTrue(this)
        }

    }

    private fun displayTrueNews() {
        // Retrieve the true news list
        val trueNewsList = retrieveTrueNews()

        // Add the content of the true news list to the textview
        for (news in trueNewsList) {
            val title = news[0]
            val text = news[1]
            val domain = news[2]
            val validity = news[3]
            val identifier = news[4]
            val rating = news[5]
            textView.append("$title\n\n$text\n\n$domain\n\n$validity\n\n$identifier\n\n$rating\n\n")
        }
    }

    private fun retrieveTrueNews(): List<Array<String>> {
        val trueNewsList = mutableListOf<Array<String>>()

        try {
            val path = Environment.getExternalStorageDirectory().path + "/True_DB.csv"
            val reader = CSVReader(FileReader(path))
            // Skip the heading using the readNext function:
            reader.readNext()
            var row: Array<String>?
            while (reader.readNext().also { row = it } != null) {
                trueNewsList.add(row!!)
            }
        } catch (e: Exception) {
            e.printStackTrace()
            textView.text = "Error retrieving data from file"
        }

        if (trueNewsList.isEmpty()) {
            textView.text = "File is empty"
        }

        return trueNewsList
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
            displayTrueNews()
        }
    }

    companion object {
        private const val PERMISSION_REQUEST_CODE = 1
    }

    fun offlineRetrieveTrue(context: Context) {
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
            displayTrueNews()
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

    interface TrueNewsService {
        @GET("/true_news")
        fun getNews(): Call<List<AllNews.News>>
    }
}