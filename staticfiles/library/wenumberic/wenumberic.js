function WeNumberic(selector, config) {
    var elements = document.querySelectorAll(selector);

    //init
    var setting = {
        stepvalue: 1,
        minvalue: 0,
        maxvalue: 99,
        onIncrease: null,
        onReduce: null
    };

    var reducedButton = '<button class="reduced items-count" type="button"></button>';
    var increaseButton = '<button class="increase items-count" type="button"></button>';

    var init = function() {
        elements.forEach( (item) => {
            //add html button reduce and increase
            item.insertAdjacentHTML( 'beforeend', increaseButton );
            item.insertAdjacentHTML( 'afterbegin', reducedButton );

            let qty = item.querySelector(".qty");
            //in case start value is null or less than minvalue or greater than maxvalue
            if((parseFloat(qty.value.trim()) < setting.minvalue) || parseFloat(qty.value) == null) {
                qty.value = setting.minvalue;
            }

            if(parseFloat(qty.value.trim()) > setting.maxvalue) {
                qty.value = setting.maxvalue;
            }

            var reduceBtn = item.querySelector(".reduced");
            var increaseBtn = item.querySelector(".increase");

            reduceBtn.addEventListener("click", function() {
                var minLimitValue = setting.minvalue + setting.stepvalue;
                if(parseFloat(qty.value.trim()) >= minLimitValue) {
                    qty.value = parseFloat(qty.value) - setting.stepvalue;
                }

                if (setting.onReduce) {
                    setting.onReduce();
                }
            });

            increaseBtn.addEventListener("click", function() {
                var maxLimitValue = setting.maxvalue - setting.stepvalue;
                if(parseFloat(qty.value.trim()) <= maxLimitValue) {
                    qty.value = parseFloat(qty.value) + setting.stepvalue;
                }

                if (setting.onIncrease) {
                    setting.onIncrease();
                }
            });
        });
    };

    if (config) {
        setting.stepvalue = config.stepvalue >= 0 ? config.stepvalue : setting.stepvalue;
        setting.minvalue = config.minvalue >= 0 ? config.minvalue : setting.minvalue;
        setting.maxvalue = config.maxvalue >= 0 ? config.maxvalue : setting.maxvalue;
        setting.onIncrease = config.onIncrease !== null ? config.onIncrease : null;
        setting.onReduce = config.onReduce !== null ? config.onReduce : null;
        init();
    }

    this.show = function() {
        alert('show ne');
    };

}





