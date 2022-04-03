Create TABLE user (
user_id int NOT NULL,
first_name varchar (50),
middle_name varchar (50),
last_name varchar (50),
street_number int,
street_name varchar (50),
house_number int,
city varchar(50),
province varchar(50),
SSN int,
gender varchar(25),
email_address varchar (50), 
date_of_birth DATE,
PRIMARY KEY (user_id)
);

Create Table patient (
patient_id int NOT NULL,
insurance int,
health_card_no int,
user_id int,
primary KEY (patient_id),
foreign key (user_id) references user (user_id) 
);

CREATE TABLE employee (
  employee_id int NOT NULL,
  employee_type varchar(50) ,
  salary int,
  user_id int, 
  PRIMARY KEY (employee_id),
  foreign key (user_id) references user (user_id));
  
Create Table phone_number(
phone_number varchar(20),
user_id int,
Primary KEY (phone_number, user_id),
Foreign Key (user_id) references user (user_id)
);

Create Table branch(
branch_id int NOT NULL,
city varchar (50),
manager_id int,
primary key (branch_id),
foreign key (manager_id) references employee (employee_id)
);


CREATE TABLE appointment (
  appointment_id int NOT NULL,
  employee_id int,
  patient_id int,
  starttime time,
  appointment_date date,
  endtime time,
  appointment_type varchar(25),
  status varchar(25),
  room_assigned int,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (employee_id) REFERENCES employee (employee_id),
  FOREIGN KEY (patient_id) REFERENCES patient (patient_id));

  
  
  CREATE TABLE appointment_procedure (
  procedure_id int NOT NULL,
  appointment_id int, 
  procedure_date date,
  invoice_id int,
  procedure_code int ,
  procedure_type varchar(100) ,
  description varchar(500) DEFAULT NULL,
  tooth_involved varchar(100) DEFAULT NULL,
  amount_of_procedure int DEFAULT NULL,
  patient_charge int DEFAULT NULL,
  insurance_charge int DEFAULT NULL,
  total_charge int DEFAULT NULL,
  bill_id int,
  PRIMARY KEY (procedure_id),
  Foreign key (appointment_id) references appointment (appointment_id));
  FOREIGN KEY (invoice_id) REFERENCES invoice (invoice_id);
  FOREIGN KEY (bill_id) REFERENCES patient_billing (bill_id);
 

  create table review(
  review_id int NOT NULL,
  communication VARCHAR(500),
  professionalism varchar(500),
  cleanliness varchar(500),
  value int,
  patient_id int,
  primary key (review_id),
  foreign key (patient_id) references patient (patient_id)
  );
  
  CREATE TABLE treatment (
  treatment_id int NOT NULL,
  treatment_type varchar(20),
  appointment_type int, 
  primary key(treatment_id),
  foreign key (appointment_type) references appointment_procedure (procedure_id)
  );
  
  CREATE TABLE fee_charge (
  fee_id int NOT NULL,
  procedure_id int DEFAULT NULL,
  fee_code int DEFAULT NULL,
  charge int DEFAULT NULL,
  PRIMARY KEY (fee_id),
  foreign key (procedure_id) references appointment_procedure (procedure_id));
  
  
  CREATE TABLE invoice (
  invoice_id int NOT NULL,
  patient_id int DEFAULT NULL,
  date_of_issue date DEFAULT NULL,
  patient_charge int DEFAULT NULL,
  insurance_charge int DEFAULT NULL,
  total_fee_charge int DEFAULT NULL,
  discount int DEFAULT NULL,
  penalty int DEFAULT NULL,
  insurance_claim_id int DEFAULT NULL,
  PRIMARY KEY (invoice_id),
  foreign key (patient_id) references patient (patient_id),
  foreign key (insurance_claim_id) references insurance_claim (claim_id)
  ); 

CREATE TABLE insurance_claim (
claim_id int NOT NULL, 
claim_amount int, 
insurance_company varchar(50),
primary key (claim_id) 
);
  
  CREATE TABLE patient_billing (
  bill_id int NOT NULL,
  appointment_id int DEFAULT NULL,
  patient_portion int DEFAULT NULL,
  insurance_portion int DEFAULT NULL,
  insurance_claim_id int DEFAULT NULL,
  payment_type varchar(20) DEFAULT NULL,
  total_amount int DEFAULT NULL,
  PRIMARY KEY (bill_id),
  Foreign key (appointment_id) references appointment (appointment_id);
  FOREIGN KEY (insurance_claim_id) REFERENCES insurance_claim (claim_id)); 
  
  CREATE TABLE patient_record (
  patient_record_id int NOT NULL,
  patient_id int,
  medication varchar(100) DEFAULT NULL,
  symptoms varchar(100) DEFAULT NULL,
  tooth varchar(100) DEFAULT NULL,
  comments varchar(100) DEFAULT NULL,
  treatment_id int DEFAULT NULL,
  primary key(patient_record_id, patient_id), 
  foreign key (patient_id) references patient (patient_id),
  foreign key (treatment_id) references treatment (treatment_id)); 
  
  
  
