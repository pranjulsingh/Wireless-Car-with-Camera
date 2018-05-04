#include <Wire.h>

int motor_one_pin1 = 12;
int motor_one_pin2 = 13;
int motor_two_pin1 = 7;
int motor_two_pin2 = 8;
int active_control=0;
int motor_one_speed = 0;
int motor_two_speed = 0;
int m1p1 = 0;
int m1p2 = 0;
int m2p1 = 0;
int m2p2 = 0;

#define SLAVE_ADDRESS 0x04
#define DC_MOTOR_ONE 201
#define DC_MOTOR_TWO 202
#define BOT_FORWARD 225
#define BOT_BACKWARD 226
#define BOT_LEFT 227
#define BOT_RIGHT 228
#define BOT_STOP 229






void botForward(){
  digitalWrite(motor_one_pin1, HIGH);
  digitalWrite(motor_two_pin1, HIGH);
  digitalWrite(motor_one_pin2, LOW);
  digitalWrite(motor_two_pin2, LOW);
}

void botBackward(){
  digitalWrite(motor_one_pin1, LOW);
  digitalWrite(motor_two_pin1, LOW);
  digitalWrite(motor_one_pin2, HIGH);
  digitalWrite(motor_two_pin2, HIGH);
}

void botLeft(){
  digitalWrite(motor_one_pin1, LOW);
  digitalWrite(motor_two_pin1, HIGH);
  digitalWrite(motor_one_pin2, LOW);
  digitalWrite(motor_two_pin2, LOW);
}

void botRight(){
  digitalWrite(motor_one_pin1, HIGH);
  digitalWrite(motor_two_pin1, LOW);
  digitalWrite(motor_one_pin2, LOW);
  digitalWrite(motor_two_pin2, LOW);
}

void botStop(){
  digitalWrite(motor_one_pin1, LOW);
  digitalWrite(motor_two_pin1, LOW);
  digitalWrite(motor_one_pin2, LOW);
  digitalWrite(motor_two_pin2, LOW);
}
// callback for received data
void receiveData(int byteCount){
  int no=0;
  while(Wire.available()) {
    no = Wire.read();
  }
  if(no>200){
    switch(no){
      case BOT_FORWARD :
        botForward();
        break;
      case BOT_BACKWARD :
        botBackward();
        break;
      case BOT_LEFT :
        botLeft();
        break;
      case BOT_RIGHT :
        botRight();
        break;
      case BOT_STOP :
        botStop();
        break;
      default :
        //active_control=no;
        break;
    }
  }
  else{
    switch(false){
      case DC_MOTOR_ONE :
        motor_one_speed=no;
        break;
      case DC_MOTOR_TWO :
        motor_two_speed=no;
        break;
      default :
        
        break;
    }
  }
}

// callback for sending data
void sendData(){
  Wire.write(active_control);
}

void setup() {
  Serial.println("Initilizing System...");
  pinMode(motor_one_pin1, OUTPUT);
  pinMode(motor_two_pin1, OUTPUT);
  pinMode(motor_one_pin2, OUTPUT);
  pinMode(motor_two_pin2, OUTPUT);
  Serial.begin(9600);
  // start serial for output
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  init1();
  Serial.println("System Ready!");
}

void loop() {
  Serial.println(motor_one_speed);
  Serial.println(motor_two_speed);
  delay(250);
}



