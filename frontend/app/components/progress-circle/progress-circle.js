angular.module('myApp')
.directive('progressCircle', [function(){
        return {
            scope: {
                percent: '=progressCircle'
            },
            template: '<div class="progress-circle"></div>',
            link: function($scope, iElm, iAttrs, controller) {
                var firstTime = true;
                $scope.$watch('percent', function(newVal) {
                    if (newVal){
                        $(iElm).find('.progress-circle').circleProgress({
                            value: $scope.percent,
                            animation: firstTime,
                            fill: { gradient: ['#ff1e41', '#ff5f43'] }
                        });
                        firstTime = false;
                    }

                });



            }
        }
    }]);