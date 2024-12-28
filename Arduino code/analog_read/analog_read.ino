void setup() {
  // put your setup code here, to run once:
pinMode(A0, INPUT);
Serial.begin(9600);
}

void loop() {
  long  sum_a = 0;
  double  avg_a = 0;
  int i,a;
  // put your main code here, to run repeatedly:
  for (i=0; i<100; i++)
  {
    
    a=analogRead(A0);
    sum_a = a + sum_a;
  }
  avg_a = sum_a/100;
  Serial.print(avg_a);
  Serial.print(",");

  delay(1000);
}
