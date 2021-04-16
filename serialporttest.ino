void setup() {
 Serial.begin(9600);
 Serial.setTimeout(1);
 pinMode(2, INPUT_PULLUP);
 pinMode(3, INPUT_PULLUP);
}
 
void loop() {
 //while (!Serial.available());
 int b1Press = digitalRead(2);
 int b2Press = digitalRead(3);
 String output = String(b1Press)+String(b2Press);
 Serial.println(output);
}
