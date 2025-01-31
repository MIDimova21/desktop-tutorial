document.addEventListener('DOMContentLoaded', () => {
            const productDropdown = document.getElementById('product');
            const timeInput = document.getElementById('time');
            const totalPriceOutput = document.getElementById('total-price');
            const totalConsumptionOutput = document.getElementById('total-consumption');

            const productMultipleSelect = document.getElementById('appliance')
            const dailyPriceOutput = document.getElementById('daily-price')
            const dailyConsumptionOutput = document.getElementById('daily-consumption')


            function calculate() {
                const [price1kWh, consumptionPerHour] = productDropdown.value.split('|').map(parseFloat);
                const timeSpent = parseFloat(timeInput.value) || 0;
                const totalPrice = price1kWh * timeSpent;
                const totalConsumption = consumptionPerHour * timeSpent;
                totalPriceOutput.textContent = totalPrice.toFixed(2);
                totalConsumptionOutput.textContent = totalConsumption.toFixed(2);
            }

            function calculateDaily() {
                const selectedOptions = Array.from(productMultipleSelect.selectedOptions);
                let totalDailyPrice = 0;
                let totalDailyConsumption = 0;

                selectedOptions.forEach(option => {
                    const [price1kWh, consumptionPerHour, dailyUsage] = option.value.split('|').map(parseFloat);
                    totalDailyPrice += price1kWh * dailyUsage;
                    totalDailyConsumption += consumptionPerHour * dailyUsage;
                });


                dailyPriceOutput.textContent = totalDailyPrice.toFixed(2);
                dailyConsumptionOutput.textContent = totalDailyConsumption.toFixed(2);
            }

            productDropdown.addEventListener('change', calculate);
            timeInput.addEventListener('input', calculate);

            productMultipleSelect.addEventListener('change', calculateDaily)
});
