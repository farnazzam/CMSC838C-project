using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using GoogleCalendarUnity;

public class Testing : MonoBehaviour
{


void Start()
{
    Calendar calendar = new Calendar();
    // var test = new List<string[]>();
    var test = calendar.Main("2119");
    Debug.Log(test[0][1]);
}





}
