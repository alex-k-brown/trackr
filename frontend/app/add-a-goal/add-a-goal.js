'use strict';

angular.module('myApp.addAGoal', ['ngRoute', 'restangular'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/view2', {
            templateUrl: 'view2/view2.html',
            controller: 'View2Ctrl'
        })
    }])


    .controller('AddAGoalCtrl', ['Restangular', '$scope', '$routeParams', '$location', function (Restangular, $scope, $routeParams, $location) {
        $scope.goal = {
            childGoals: [],
            dueDate: new Date()
        };
        // GET a list of all timeFrames
        Restangular.all('goals').getList().then(function (timeFrames) {
            $scope.timeFrame = timeFrames;
        })

//        $scope.calculateDueDate = function(timeFrame.days){
//
//            $scope.goal.dueDate.setDate($scope.goal.dueDate.getDate() + (timeFrame.days));
//        }

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

        $scope.dateOptions = {
            formatYear: 'yy',
            startingDay: 1
        };

//            $scope.initDate = new Date('2016-15-20');
        $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
        $scope.format = $scope.formats[0];
        $scope.steps = []

        $scope.addStep = function () {
//            Restangular.one('goals', $scope.goalId).customPOST($scope.goal).then(function (data) {
//                    $scope.status = "This step was successfully added";
//                    $scope.goal = data;
//                    $location.path('/goals');
//                }, function () {
//                    $scope.status = "This step couldn't be added";
//                }
//            )
            $scope.goal.childGoals.push($scope.childGoal.step)
            $scope.childGoal.step = ""
        };

        $scope.deleteStep = function () {
            if (confirm("Are you sure you want to delete this step?")) {
                Restangular.one('goals', $scope.goalId).customDELETE().then(function () {
                    $location.path('/goals');
                }, function () {
                    $scope.status = "The step couldn't be deleted";
                });
            }

        };

        $scope.addGoal = function () {
            Restangular.one('add-goal/').customPOST($scope.goal).then(function (data) {
                    $scope.status = "Your goal was successfully added";
                    $scope.goal = data;
                    $location.path('/goals');
                }, function () {
                    $scope.status = "Your goal couldn't be saved";
                }
            )
        }

    }])


