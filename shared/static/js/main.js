
/**
 * Create a Chartjs Chart
 * @param  {String} selector
 * @param  {Object} data    
 */
function createChart(selector, data){
	var canvas = document.querySelector(selector);
	if(!canvas) return;
	canvas.width = 1000;
	var ctx = canvas.getContext("2d");
	var dashboardChart = new Chart(ctx).Bar(data, {});
}

createChart('.estimations-canvas', {
	labels: ["January", "February", "March", "April", "May", "June", "July"],
	datasets: [{
		fillColor: "rgba(220,220,220,0.5)",
		strokeColor: "rgba(220,220,220,1)",
		data: [65, 59, 90, 81, 56, 55, 40]
	}]
});

createChart('.members-canvas', {
	labels: ["January", "February", "March", "April", "May", "June", "July"],
	datasets: [{
		fillColor: "rgba(151,187,205,0.5)",
		strokeColor: "rgba(151,187,205,1)",
		data: [28, 3, 40, 19, 96, 27, 12]
	}]
});