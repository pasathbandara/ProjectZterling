package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.drawerlayout.widget.DrawerLayout
import com.google.android.material.navigation.NavigationView

class TopPage : AppCompatActivity() {
    lateinit var toggle: ActionBarDrawerToggle

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_top_page)

        val drawerLayout : DrawerLayout = findViewById(R.id.drawerLayout)
        val navView : NavigationView = findViewById(R.id.nav_view)
        toggle = ActionBarDrawerToggle(this,drawerLayout,R.string.open,R.string.close)
        drawerLayout.addDrawerListener(toggle)
        toggle.syncState()

        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        navView.setNavigationItemSelectedListener {
            when(it.itemId){
                R.id.nav_lates -> Toast.makeText(applicationContext,
                    "Home", Toast.LENGTH_SHORT).show()
                R.id.nav_faq -> Toast.makeText(applicationContext,
                    "Profile", Toast.LENGTH_SHORT).show()
                R.id.nav_top -> Toast.makeText(applicationContext,
                    "Logout", Toast.LENGTH_SHORT).show()
                R.id.nav_stories -> Toast.makeText(applicationContext,
                    "Rating", Toast.LENGTH_SHORT).show()
                R.id.nav_factcheck -> Toast.makeText(applicationContext,
                    "Settings", Toast.LENGTH_SHORT).show()
                R.id.nav_language -> Toast.makeText(applicationContext,
                    "Share", Toast.LENGTH_SHORT).show()
            }
            true
        }
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        if(toggle.onOptionsItemSelected(item)){
            return true
        }
        return super.onOptionsItemSelected(item)
    }
}