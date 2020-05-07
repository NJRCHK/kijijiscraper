public Class CarInfo{
	private String make;
	private String model; 
	private int price;
	private String condition;
	private int kilometres;
	private String transmission;
	private String driveTrain;
	private String fuelType;
	
	public CarInfo(){
		make = "N/A";
		model = "N/A";
		price = 0;
		condition = "N/A";
		kilometres = 0;
		transmission = "N/A";
		driveTrain = "N/A"
		fuelType = "N/A"
	}
	
	public string getMake(){
		return make;
	}
	
	public void setMake(String make){
		this.make = make;
	}
	
	public string getModel(){
		return model;
	}
	
	public void setModel(String model){
		this.model = model;
	}
	
	public int getPrice(){
		return price;
	}
	
	public void setPrice(int price){
		this.price = price;
	}
	
	public String getCondition(){
		return condition;
	}
	
	public void setCondition(String condition){
		this.condition = condition;
	}
	
	public int getKilometres(){
		return kilometres;
	}
	
	public void setKilometres(int kilometres){
		this.kilometres = kilometres;
	}
	
	public String getTransmission(){
		return transmission;
	}
	
	public void setTransmission(String transmission){
		this.transmission = transmission;
	}
	
	public String getDriveTrain(){
		return driveTrain;
	}
	
	public void setDriveTrain(String driveTrain){
		this.driveTrain = driveTrain;
	}
	
	public String getFuelType(){
		return fuelType;
	}
	
	public void setFuelType(String fuelType){
		this.fuelType = fuelType;
	}
	
	public toString(){
		String s = make + "," + model + "," + price + "," +
		condition + "," + kilometres + "," + transmission +
		"," +  driveTrain + "," + fuelType;
		return s;
	}
}