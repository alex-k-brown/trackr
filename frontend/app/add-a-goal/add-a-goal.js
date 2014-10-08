'use strict';

angular.module('myApp.addAGoal', ['ngRoute', 'restangular'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/add-a-goal', {
            templateUrl: 'add-a-goal/add-a-goal.html',
            controller: 'AddAGoalCtrl'
        })
    }])


    .controller('AddAGoalCtrl', ['Restangular', '$scope', '$routeParams', '$location', function (Restangular, $scope, $routeParams, $location) {
        var today = new Date();
        $scope.goal = {
            childGoals: [],
            dueDate: today.toDateString()
        };
        // GET a list of all goals in the database
        Restangular.all('goals').getList().then(function (goals) {
            $scope.goals = goals;
        });


        $scope.calculateDueDate = function (days) {
            var result = new Date();
            var daysNumber = (isNaN(parseInt(days))) ? 0 : parseInt(days);
            result.setDate(result.getDate() + daysNumber);
            $scope.goal.dueDate = result.toDateString();
//
        };
        //Datepicker functionality
//        $scope.today = function () {
//            $scope.dt = new Date();
//        };
//        $scope.today();//today

//            $scope.clear = function () {
//                $scope.dt = null;
//            };
//            $scope.toggleMin = function () {
//                $scope.minDate = $scope.minDate ? null : new Date();
//            };
//            $scope.toggleMin();
//
//            $scope.open = function ($event) {
//                $event.preventDefault();
//                $event.stopPropagation();
//
//                $scope.opened = true;
//            };

//        $scope.dateOptions = {
//            formatYear: 'yy',
//            startingDay: 1
//        };
//
//        $scope.initDate = new Date('2016-15-20');
//        $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
//        $scope.format = $scope.formats[0];
//        $scope.steps = [];

        $scope.addStep = function () {
            //Different non working functionality to add goal
//            Restangular.one('goals', $scope.goalId).customPOST($scope.goal).then(function (data) {
//                    $scope.status = "This step was successfully added";
//                    $scope.goal = data;
//                    $location.path('/goals');
//                }, function () {
//                    $scope.status = "This step couldn't be added";
//                }
//            )
            $scope.goal.childGoals.push($scope.childGoal.step);
            $scope.childGoal.step = ""
        };

        $scope.deleteStep = function (index) {
            if (confirm("Are you sure you want to delete this step?")) {
                $scope.goal.childGoals.splice(index, 1);
            }

        };

        $scope.addGoal = function () {
            var goal = angular.copy($scope.goal);
            var d = new Date(goal.dueDate);

            goal.dueDate = (d.getFullYear() + "-" + (d.getMonth() + 1)+ "-" + (d.getDate()));
            Restangular.one('add-goal/').customPOST(goal).then(function (data) {
                    $scope.status = "Your goal was successfully added";
                    $location.path('/detail-page/'  + data.id);
                }, function () {
                    $scope.status = "Your goal couldn't be saved";
                }
            )
        }

    }]);


