package com.abhishek.anudip;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.HashMap;

public class SurveyActivity extends AppCompatActivity {

    static int key = 1;

    EditText person_name , person_phone_no , person_email_id , input_1 , input_2, input_3, input_4, input_5;

    Button submit;

    FirebaseAuth auth;
    DatabaseReference reference;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_survey);

        person_name = findViewById(R.id.person_name);

        person_phone_no = findViewById(R.id.person_phone_no);

        person_email_id = findViewById(R.id.person_email_id);

        input_1 = findViewById(R.id.input_1);

        input_2 = findViewById(R.id.input_2);

        input_3 = findViewById(R.id.input_3);

        input_4 = findViewById(R.id.input_4);

        input_5 = findViewById(R.id.input_5);

        submit = findViewById(R.id.submit);

        auth = FirebaseAuth.getInstance();

        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {


                String str_person_name = person_name.getText().toString();
                String str_person_phone_no = person_phone_no.getText().toString();
                String str_person_email_id = person_email_id.getText().toString();
                String str_input_1 = input_1.getText().toString() ;
                String str_input_2 = input_2.getText().toString();
                String str_input_3 = input_3.getText().toString();
                String str_input_4 = input_4.getText().toString();
                String str_input_5 = input_5.getText().toString();


                if (TextUtils.isEmpty(str_person_name) || TextUtils.isEmpty(str_person_phone_no) || TextUtils.isEmpty(str_person_email_id)|| TextUtils.isEmpty(str_input_1) || TextUtils.isEmpty(str_input_2) || TextUtils.isEmpty(str_input_3) || TextUtils.isEmpty(str_input_4) || TextUtils.isEmpty(str_input_5)){
                    Toast.makeText(SurveyActivity.this, "All fields are required!", Toast.LENGTH_SHORT).show();
                } else {
                    addvalues(str_person_name , str_person_phone_no ,str_person_email_id,str_input_1, str_input_2,str_input_3,str_input_4,str_input_5);
                }
            }
        });
    }

    public void addvalues(String str_person_name , String str_person_phone_no , String str_person_email_id,String str_input_1,String str_input_2,String str_input_3,String str_input_4,String str_input_5){


        FirebaseUser firebaseUser = auth.getCurrentUser();
        String userID = firebaseUser.getUid();

        HashMap<String, Object> map = new HashMap<>();
        String data = Integer.toString(key);
        key++;
        data = "Data" + data;
        reference = FirebaseDatabase.getInstance().getReference().child("Users").child(userID).child(data);

        map.put("str_person_name", str_person_name);
        map.put("str_person_phone_no", str_person_phone_no);
        map.put("str_person_email_id", str_person_email_id);
        map.put("str_input_1", str_input_2);
        map.put("str_input_2", str_input_2);
        map.put("str_input_3", str_input_3);
        map.put("str_input_4", str_input_4);
        map.put("str_input_5", str_input_5);

        reference.setValue(map).addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()){
                    Intent intent = new Intent(SurveyActivity.this, ThankyouActivity.class);
                    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK | Intent.FLAG_ACTIVITY_NEW_TASK);
                    startActivity(intent);
                }
            }
        });

    }

}