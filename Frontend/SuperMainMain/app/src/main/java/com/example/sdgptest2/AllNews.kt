package com.example.sdgptest2

import android.Manifest
import android.content.pm.PackageManager
import android.os.Bundle
import android.os.Environment
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.opencsv.CSVReader
import java.io.FileReader

class AllNews : AppCompatActivity() {

    private lateinit var textView: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_all_news)
        textView = findViewById(R.id.allnewstextview)

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
}