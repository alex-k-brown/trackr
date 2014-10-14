'use strict';

angular.module('myApp.home', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: 'home/home.html',
    controller: 'HomeCtrl'
  });
}])

.controller('HomeCtrl', ['$scope', 'Restangular', function($scope, Restangular) {

        $scope.activeGoals="../app/partials/active-goals.html"
        Restangular.all('goals').getList().then(function(goals) {
            $scope.goals = goals;
            $scope.orderProp = 'duedate';
        })
        $scope.activeButton=function(goal){
            goal.clicked=!goal.clicked;
            $scope.anythingClicked=false;
            for (var i=0; i<$scope.goals.length; i++){
                var currentGoal=$scope.goals[i];
                if (currentGoal.clicked){
                    $scope.anythingClicked=true;
                }
            }
            console.log($scope.anythingClicked)
        }
}]);