package com.example.sdgptest2

import android.Manifest
import android.content.pm.PackageManager
import android.os.Build
import android.os.Bundle
import android.os.Environment
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.opencsv.CSVReader
import java.io.FileReader

class TrueNews : AppCompatActivity() {
    private lateinit var textView: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_true_news)

        textView = findViewById(R.id.truenewstextview)

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
}