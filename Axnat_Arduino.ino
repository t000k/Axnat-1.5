int led=8;
int dato;

void setup() {
  // put your setup code here, to run once:
pinMode(led, OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.setTimeout(1000);
if(Serial.available()>0){
  dato = Serial.read();

  if(dato=='P'){

    digitalWrite(led, HIGH);
    delay(300);
    digitalWrite(led, LOW);
    dato=0;
}
  if(dato=='N'){
    digitalWrite(led, LOW);
 
}


}
}
